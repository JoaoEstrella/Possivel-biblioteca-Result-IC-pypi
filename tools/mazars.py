import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Mazars:

    def __init__(self, trac = True): #
        
        self.nu = 0.20
        self.E = 27691.47
        self.ed0 = 0.000127
        
        self.trac = trac
        self.setModel()
    
    def setModel(self):
        if self.trac:
            self.epsexp = np.array([0.000010, 0.000020, 0.000029, 0.000039, 0.000047, 0.000058, 0.000067, 0.000077, 0.000086,
                                    0.000096, 0.000105, 0.000115, 0.000127, 0.000134, 0.000143, 0.000153, 0.000162, 0.000172,
                                    0.000181, 0.000191,0.000200, 0.000210, 0.000219, 0.000229, 0.000238, 0.000248, 0.000257,
                                    0.000267, 0.000276, 0.000286, 0.000295, 0.000305, 0.000314, 0.000324, 0.000350])
            
            self.sigexp = np.array([ 0.2769, 0.5400, 0.8031, 1.0661, 1.3034, 1.5874, 1.8431, 2.0913, 2.3268, 2.5420, 2.7264,
                                    2.8660, 2.8965, 2.8563, 2.7189, 2.5458, 2.3665, 2.1948, 2.0367, 1.8938, 1.7660, 1.6520,
                                    1.5505, 1.4599, 1.3788, 1.3061, 1.2406, 1.1814, 1.1277, 1.0789, 1.0342, 0.9933, 0.9558,
                                    0.9211, 0.8374])
        else:
            self.epsexp = np.array([ -0.00008, -0.00018, -0.00028, -0.00038, -0.00048, -0.00058, -0.00068, -0.00078, -0.00088,
                               -0.00098, -0.00108, -0.00118, -0.00128, -0.00138, -0.00148, -0.00158, -0.00168, -0.00178,
                               -0.00188, -0.00198, -0.00208, -0.00218, -0.00228,  -0.00238, -0.00248, -0.00258, -0.00268,
                               -0.00278, -0.00288, -0.00298, -0.00308, -0.00318, -0.00328, -0.00338, -0.0035])
            
            self.sigexp = np.array([ -2.215317267, -4.98446385, -7.753610433, -10.52275702, -13.2919036, -15.81901094, -18.15324716,
                                -20.28258044, -22.19007179, -23.86731335, -25.31358942, -26.53465875, -27.54135304, -28.34815843,
                                -28.97190329, -29.43062828, -29.74267344, -29.92598494, -29.99762379, -29.93800316, -29.69272427,
                                -29.2929163, -28.77104066, -28.1564448, -27.47471288, -26.74748726, -25.99260853, -25.2244459,
                                -24.45432104, -23.69095847, -22.94092065, -22.20900428, -21.49858727, -20.81192384, -20.02117078]) 
            
    
    
    def calc(self, ch, fit = True):
        if self.trac:
            Ac = 0
            Bc = 0
            At = ch[0]
            Bt = ch[1]
        else:
            At = 0
            Bt = 0
            Ac = ch[0]
            Bc = ch[1]
    
        Sig = np.zeros(len(self.epsexp))
        for i in range(0, len(self.epsexp)):
            Dano = 0
            epstil = 0
            Esec = 0
            aux2 = 0
            aux3 = 0
            aux4 = 0
            aux5 = 0
            if self.epsexp[i] > 0:
                epstil = self.epsexp[i]
            else:
                epstil = -self.nu * self.epsexp[i] * (2 ** 0.5)
            if epstil > self.ed0:
                if self.epsexp[i] > 0:
                    aux2 = Bt * (epstil - self.ed0)
                    aux3 = np.exp(aux2)
                    Dano = 1 - (self.ed0 * ((1.0 - At) / epstil)) - (At / aux3)
    
                elif self.epsexp[i] < 0:
                    aux4 = Bc * (epstil - self.ed0)
                    aux5 = np.exp(aux4)
                    Dano = 1 - (self.ed0 * ((1.0 - Ac) / epstil)) - (Ac / aux5)
    
                if Dano > 0.99:
                    Dano = 0.99
                elif Dano < 0.00:
                    Dano = 0
    
            Esec = self.E * (1 - Dano)
            Sig[i] = self.epsexp[i] * Esec
            
        if fit == False:
            return Sig
        
        dist = (self.sigexp - Sig) / self.sigexp
        valor_fo = dist ** 2
        
        return (sum(valor_fo)) ** 0.5

    
    def plot(self):
        
        fig, ax, = plt.subplots(figsize=(16, 8))
        
        ax.grid()
        ax.scatter(self.epsexp*10**4, self.sigexp, label='Exp')
        #ax.scatter(self.epsexp*10**4, self.calc(ch, False), label = 'Modelo')
        ax.set(xlabel='Strain * 10-4', ylabel='Stress (mPa)')
        ax.legend()
        
        
        '''
        fig, ax, = plt.subplots(figsize=(16, 10))
        xX = np.arange(nGen)
       
        #cada gen
            ax.plot(xX, oFunc, label='fBest '+str(nR))
            # ax.set_ylim(0,47636580) #zoom
            ax.grid()
            ax.legend(fontsize='x-large')
            ax.set(xlabel='GENS', ylabel='FO', title='JOAO')
        plt.show() 
        '''

    def plots(self, chs, nome, trac = True):
        self.trac = trac
        self.setModel()
        
        fig, (ax, ax2), = plt.subplots(figsize=(32, 16), dpi=20)
        msize = 3500
        alp = 1
        
        for meta, ch in chs.items():
            ax.scatter(self.epsexp*10**4, self.calc(ch[:-1], False), alpha = alp, facecolors="None", edgecolor=ch[-1],
                       label = meta, s=msize, linewidth=2)
            
            ax.scatter(self.epsexp*10**4, self.calc(ch[:-1], False),c =ch[-1], s= 10)
            
            #plt.plot(self.epsexp*10**4, self.calc(ch[:-1], False), 'o', ms=50, markerfacecolor="None",
            #         markeredgecolor=ch[-1], markeredgewidth=2, label = meta)

            msize *= 0.2
       
        ax.scatter(self.epsexp*10**4, self.sigexp, marker='3', edgecolor='black',c='black', linewidth=10, s=3000,
                   edgecolors='blue', label='EXPERIMENTAL', alpha=0.5)
        
        ax.scatter(self.epsexp*10**4,self.sigexp ,c ='black', s= 10)
        
        ax.set_xlabel('$\epsilon$ $x 10^{-4}$',fontsize=40)
        ax.set_ylabel('$\sigma$ $(MPa)$', fontsize=40)
        ax.xaxis.set_tick_params(labelsize=30)
        ax.yaxis.set_tick_params(labelsize=30)
        ax.legend(fontsize=30, labelspacing=1, borderpad=1, shadow=True)
        ax.grid(alpha=0.2, linewidth=5)
                
        ax.patch.set_edgecolor('black')  
        ax.patch.set_linewidth(2)
        fig.savefig('wander/'+nome+'.jpeg', dpi=200)
                
    def r2(self, ch, trac = True):
        self.trac = trac
        self.setModel()
        
        real = self.sigexp          
        est = self.calc(ch, False)   
        
        n = sum( (real - real.mean()) * (est - est.mean()) )
        d1 = sum( (est - est.mean())**2)**0.5
        d2 = sum( (real - real.mean())**2)**0.5
        
        rr = (n/(d1*d2))
        rQ = rr**2
            
        
        n = sum ( (est - real)**2 )
        d1 = sum ( (abs(est - real.mean()) + abs(real - real.mean()))**2)
        
        d = (1- (n/d1))
            
        pi = d*(rQ)**0.5
        
        mae = sum(abs(real - est))/len(real)
        
        rmse = (sum((real - est)**2)/len(real))**0.5
            
        return {'r':rr, 'r2':rQ, 'd':d, 'pi':pi, 'mae':mae, 'rmse':rmse}

    def plott(self, nome, trac = False):
        #ordem: trac, comp
        self.trac = trac
        self.setModel()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))

        
        for ax in [ax1, ax2]:
            msize = 1000
            alp = 1
            msize *= 0.2

            ax.scatter(self.epsexp*10**4, self.sigexp, marker='3', edgecolor='black',c='black', linewidth=2, s=1000,
                       edgecolors='blue', label='EXPERIMENTAL', alpha=0.5)

            ax.scatter(self.epsexp*10**4,self.sigexp ,c ='black', s= 5)

            ax.set_xlabel('$\epsilon$ $x 10^{-4}$',fontsize=20)
            if self.trac:
                ax.set_ylabel('$\sigma$ $(MPa)$', fontsize=20)
                ax.yaxis.set_tick_params(labelsize=12)
            ax.xaxis.set_tick_params(labelsize=12)
            
           # ax.legend(fontsize=10, labelspacing=1, borderpad=1, shadow=True)
            ax.grid(alpha=0.2, linewidth=2)
            ax.margins(0.1)

            ax.patch.set_edgecolor('black')  
            ax.patch.set_linewidth(1)
            
            #trocando
            self.trac = True
            self.setModel()
            
        lines_labels = [ax.get_legend_handles_labels()]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]

        # finally we invoke the legend (that you probably would like to customize...)

        fig.legend(lines, labels, loc=(0.8, 0.91))
        fig.savefig('wander/'+nome+'.svg', dpi=500, bbox_inches="tight", transparent=True)
        
    def plots2(self, chs1, chs2, nome, trac = True, trac2=False):
        #ordem: trac, comp
        self.trac = trac
        self.setModel()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))

        
        for ax, chs, in zip([ax1, ax2], [chs1, chs2]):
            msize = 1000
            alp = 1
            for meta, ch in chs.items():
                ax.scatter(self.epsexp*10**4, self.calc(ch[:-1], False), alpha = alp, facecolors="None", edgecolor=ch[-1],
                           label = meta, s=msize, linewidth=2)

                ax.scatter(self.epsexp*10**4, self.calc(ch[:-1], False),c =ch[-1], s= 0.5)

                #plt.plot(self.epsexp*10**4, self.calc(ch[:-1], False), 'o', ms=50, markerfacecolor="None",
                #         markeredgecolor=ch[-1], markeredgewidth=2, label = meta)

                msize *= 0.2

            ax.scatter(self.epsexp*10**4, self.sigexp, marker='3', edgecolor='black',c='black', linewidth=2, s=1000,
                       edgecolors='blue', label='EXPERIMENTAL', alpha=0.5)

            ax.scatter(self.epsexp*10**4,self.sigexp ,c ='black', s= 5)

            ax.set_xlabel('$\epsilon$ $x 10^{-4}$',fontsize=20)
            if True:#self.trac:
                ax.set_ylabel('$\sigma$ $(MPa)$', fontsize=20)
                ax.yaxis.set_tick_params(labelsize=12)
            ax.xaxis.set_tick_params(labelsize=12)
            
            #ax.legend(fontsize=10, labelspacing=1, borderpad=1, shadow=True)
            ax.grid(alpha=0.2, linewidth=2)

            ax.patch.set_edgecolor('black')  
            ax.patch.set_linewidth(1)
            
            ax.margins(0.1) 
            
            #trocando
            self.trac = trac2
            self.setModel()
        
        lines_labels = [ax.get_legend_handles_labels()]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]

        fig.legend(lines, labels, loc=(0.62, 0.91), ncol=4,
           frameon=False)
        fig.savefig('wander/'+nome+'.svg', dpi=500, bbox_inches="tight", transparent=True)