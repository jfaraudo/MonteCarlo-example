set xlabel "Number of MC trials"
set ylabel "Estimated value of Pi"

# Funcio a ajustar
l(x)=n
set xrange[80000:100000]
# fit
fit l(x) "MCpi.dat" u 1:2 via n

set xrange[0:100000]

plot "MCpi.dat" u 1:2 w l notitle,l(x) w l t sprintf("Average (from 80000): %.5f",n)
