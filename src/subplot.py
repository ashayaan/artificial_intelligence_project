import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def subPlots(access,alpha,beta,flex,hydro,retention):
	fig, (ax1,ax2, ax3, ax4, ax5, ax6) = plt.subplots(6)
	ax1.set_color_cycle('navy')
	ax2.set_color_cycle('firebrick')
	ax3.set_color_cycle('darkgreen')
	ax4.set_color_cycle('navy')
	ax5.set_color_cycle('firebrick')
	ax6.set_color_cycle('darkgreen')
	
	fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
	ax1.plot(access)
	ax2.plot(alpha)
	ax3.plot(beta)
	ax4.plot(flex)
	ax5.plot(hydro)
	ax6.plot(retention)
	
	ax1.set(title='Accessible residues', xlabel = 'Position', ylabel='Score')
	ax2.set(title='Alpha helix', xlabel = 'Position', ylabel='Score')
	ax3.set(title='Beta turn', xlabel = 'Position', ylabel='Score')
	ax4.set(title='Average flexibility', xlabel = 'Position', ylabel='Score')
	ax5.set(title='Hydrophbicity', xlabel = 'Position', ylabel='Score')
	ax6.set(title='TFA retention', xlabel = 'Position', ylabel='Score')

	# ax1.set_color('black')
	# plt.grid()
	plt.show()



if __name__ == '__main__':
	df = pd.read_csv('../data_files/plot.csv',header=None)

	access = np.array(list(df.iloc[0]))
	alpha = np.array(list(df.iloc[1]))
	beta = np.array(list(df.iloc[2]))
	flex = np.array(list(df.iloc[3]))
	hydro = np.array(list(df.iloc[4]))
	retention = np.array(list(df.iloc[5]))

	subPlots(access,alpha,beta,flex,hydro,retention)