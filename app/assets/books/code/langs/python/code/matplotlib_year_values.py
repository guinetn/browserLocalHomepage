import matplotlib.pyplot as p
year = [1950,1970,1990,2010]
pop= [2.519,3.692,5.263,6.972]
p.plot(year,pop)	
p.show()

p.scatter(x,y)		# Put the x-axis on a logarithmic scale
p.xscale('log') 		# logarithmic scale.