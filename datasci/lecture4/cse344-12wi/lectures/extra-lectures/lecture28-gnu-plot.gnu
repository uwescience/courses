# Let s0 be the desire threshold
# That is, we want to find pairs of documents whose Jaccard similarity is > s0
#
#    return { (d1,d2) | J(d1,d2) > s0}

s0 = 0.8

# Instead of computing all Jaccard similarties, we compute the min-hashes,
# then the LSH, and therefore each document d has a signature SIG(d).
# We return the pairs of documents that have a common signature:
#
#   return { (d1,d2) | SIG(d1) intersect SIG(d2) != emptyset }
#
# The probability of two documents have the same signature is:
#
#    p = P[SIG(d1) = SIG(d2)] =  1-(1-s^r)^b
#
# The curve has a huge jump from ~ 0 to ~ 1 at s = (1/b)^(1/r)
# Thus, we want to have:
#
#    (1/b)^(1/r) = s0
# 
# This gives us r as a function of b and s0
#

r(b,s0) = log(b)/log(1/s0)

# now we can compute p =  1-(1-s^r)^b

p(s,b) = 1-exp(b*log(1-exp(r(b,s0)*log(s))))

# the total number of min-hashes is b*r
m(b) = b*r(b,s0)

# we try this for 10 values of b, growing them exponentially
# c = exponential growth rate (try c = 1,2,3,4)

c = 1
b(n) = exp(c*n)
set xrange [ 0 : 1 ]
titlen(n) = sprintf("Bands b=%d; size r=%d; minhashes m=%d",b(n), r(b(n),s0), m(b(n)))

plot for [n=1:10] p(x,b(n)) title titlen(n)
