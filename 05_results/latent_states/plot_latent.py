"""Rebuild the two manuscript data figures. Run in the directory containing the three NPZs."""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.lines import Line2D
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch

OUT = Path(__file__).resolve().parent
ORANGE, PEACH, GRAY, BLACK = '#eb6834', '#f6b48f', '#8a8984', '#181818'
plt.rcParams.update({'font.family':'sans-serif','font.sans-serif':['Arial','Liberation Sans','DejaVu Sans'], 'font.size':8,
    'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#8a8984','axes.linewidth':.6,
    'axes.labelsize':8,'xtick.labelsize':7,'ytick.labelsize':7,'xtick.color':'#52514e','ytick.color':'#52514e',
    'xtick.major.size':2.5,'ytick.major.size':2.5,'legend.frameon':False,'pdf.fonttype':42,'ps.fonttype':42})

def axes(ax):
    ax.grid(axis='y',color='#e4e3df',lw=.5); ax.set_axisbelow(True)
    ax.margins(x=.015); ax.yaxis.set_major_locator(MaxNLocator(nbins=4))

def save(fig, name):
    for ext,opts in [('pdf',{}),('png',{'dpi':250}),('tiff',{'dpi':600,'pil_kwargs':{'compression':'tiff_lzw'}})]:
        fig.savefig(OUT/(name+'.'+ext),facecolor='white',**opts)
    plt.close(fig)

def synthetic():
    with np.load(OUT/'latent_E0.npz') as z:
        i=list(z['names']).index('STR1'); ok=z['tmask'][i].astype(bool); t=np.arange(1,ok.sum()+1)
        specs=[('Rperm_true','Rperm_hat',r'Permanent rut + datum, $\sum R_i+d_0$',ORANGE),
               ('rev_true','rev_hat',r'Recoverable component, $r$','#bb542b')]
        fig,axs=plt.subplots(1,2,figsize=(190/25.4,61/25.4)); fig.subplots_adjust(left=.085,right=.985,bottom=.2,top=.72,wspace=.32)
        fig.text(.018,.936,'(c)   Synthetic state recovery',fontsize=10,weight='bold'); fig.text(.018,.842,'STR1   /   seed 0   /   survey noise 0.10 mm',fontsize=8,color='#52514e')
        for ax,(tr,est,label,color) in zip(axs,specs):
            v=z[tr][i,ok]; w=z[est][i,ok]; ax.plot(t,v,color=BLACK,lw=1.05,ls='--',label='Simulated truth',zorder=3)
            ax.plot(t,w,color=color,lw=1.4,label='Filtered estimate'); axes(ax); ax.set_title(label,loc='left',fontsize=8,weight='bold'); ax.set_ylabel('Rut depth (mm)'); ax.set_xlabel('Survey occasion')
        fig.legend([Line2D([],[],color=BLACK,ls='--'),Line2D([],[],color=ORANGE)],['Simulated truth','Filtered estimate'],ncol=2,loc='upper right',bbox_to_anchor=(.99,.989),fontsize=7.5)
        save(fig,'Fig4c-Synthetic-recovery')
        with (OUT/'Fig4c-source.csv').open('w',newline='') as f:
            wr=csv.writer(f); wr.writerow(['structure','survey','permanent_plus_datum_true_mm','permanent_plus_datum_filtered_mm','recoverable_true_mm','recoverable_filtered_mm']); wr.writerows(zip(['STR1']*len(t),t,*(z[k][i,ok] for k in ['Rperm_true','Rperm_hat','rev_true','rev_hat'])))

def real():
    ids=['STR1','STR4','STR7','STR10','STR13','STR15','STR18']; labels=['I   Semi-rigid','II   Rigid composite','III   Semi-rigid','IV   Inverted','V   Thick AC','VI   Thick AC','VII   Full-depth AC']
    cmap=LinearSegmentedColormap.from_list('depth',['#fce3c7','#f8ac7b','#e27747','#b24b2d','#78331f'])
    with np.load(OUT/'latent_E3.npz') as z, (OUT/'Real-source.csv').open('w',newline='') as f, (OUT/'Sublayer-source.csv').open('w',newline='') as sf:
        wr=csv.writer(f); sw=csv.writer(sf); wr.writerow(['class','structure','fold','survey','cumulative_ESAL_million','survey_mm','filtered_sum_mm','permanent_mm','datum_mm','recoverable_mm','survey_minus_filtered_mm']); sw.writerow(['structure','survey','cumulative_ESAL_million','sublayer_from_surface','mid_depth_mm','thickness_mm','permanent_rut_mm'])
        fig,axs=plt.subplots(7,3,figsize=(190/25.4,235/25.4),sharex=True,sharey='col'); fig.subplots_adjust(left=.148,right=.99,top=.896,bottom=.083,hspace=.24,wspace=.23)
        fig.text(.015,.97,'Filtered rut components across seven pavement classes',fontsize=11,weight='bold'); fig.text(.015,.945,'Held-out structure classes  /  one representative per class  /  seed 0',color='#52514e')
        for ax,title in zip(axs[0],['Survey and filtered total','Datum and recovery','Permanent rut by sublayer']): ax.set_title(title,loc='left',fontsize=8,weight='bold',pad=8)
        for j,(n,cl) in enumerate(zip(ids,labels)):
            get=lambda k:z[n+'__'+k]; x=get('N')/1e6; y,r,d,R=map(get,['y','r','d0','Rperm']); fit=R+r+d; L=get('R_layer')[:,get('lmask').astype(bool)]; h=get('h'); mid=get('zmid'); assert len(h)==L.shape[1] and np.all(np.diff(mid)>0); np.testing.assert_allclose(L.sum(axis=1),R,atol=1e-9); assert np.isfinite(np.c_[x,y,r,d,L]).all()
            a,b,c=axs[j]; a.plot(x,fit,color=ORANGE,lw=1.2); a.scatter(x,y,color=BLACK,s=2,alpha=.7,zorder=3); b.axhline(0,color='#b9b8b1',lw=.6); b.plot(x,d,color='#666561',ls='--',lw=1); b.plot(x,r,color='#c65d37',lw=1.05); c.stackplot(x,*L.T,colors=cmap(np.linspace(.04,.96,L.shape[1])),edgecolor='white',linewidth=.22); c.plot(x,R,color='#954123',lw=.65)
            for ax in (a,b,c): axes(ax); ax.tick_params(pad=2)
            a.text(-.16,.72,n,transform=a.transAxes,ha='right',fontsize=8,weight='bold'); a.text(-.16,.45,cl.replace('   ','\n'),transform=a.transAxes,ha='right',va='center',fontsize=7,linespacing=1.2,color='#52514e')
            for i in range(len(x)):
                wr.writerow([cl,n,int(get('fold')),i+1,x[i],y[i],fit[i],R[i],d[i],r[i],y[i]-fit[i]])
                for k in range(len(h)): sw.writerow([n,i+1,x[i],k+1,mid[k],h[k],L[i,k]])
        for a in axs[-1]: a.set_xlabel('Cumulative ESAL (million)'); a.xaxis.set_major_locator(MaxNLocator(4))
        handles=[Line2D([],[],ls='',marker='.',color=BLACK),Line2D([],[],color=ORANGE),Line2D([],[],color='#666561',ls='--'),Line2D([],[],color='#c65d37'),Patch(facecolor=cmap(.05)),Patch(facecolor=cmap(.95))]; fig.legend(handles,['Survey','Filtered total','Datum','Recoverable','Shallow','Deep'],loc='lower center',bbox_to_anchor=(.5,.012),ncol=6,fontsize=7.5,columnspacing=1.4); fig.text(.015,.917,'All depths and components in mm',color='#52514e',fontsize=7)
        save(fig,'Real-pavement-decomposition')

if __name__=='__main__': synthetic(); real()
