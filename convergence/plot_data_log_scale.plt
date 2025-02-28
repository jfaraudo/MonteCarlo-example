set xlabel "Number of MC trials"
set ylabel "Number of trials inside"

# Funcio a ajustar
l(x)=n
set xrange[80000:100000]
# fit
fit l(x) "MCpi.dat" u 1:2 via n

set xrange[10:100000]
set logscale x 10
plot "MCpi.dat" u 1:2 w l notitle,l(x) w l t sprintf("Average (from 80000): %.5f",n)
