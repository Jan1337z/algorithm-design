
# MAX SUM
# 

# alle Loesungen ausprobieren, O(m^3)
def max_sum_all(a):                 # m = len(a)
    # todo
    return 0


# maximale Praefixsumme, O(len(a))
#   Vorbedingung len(a) > 0
def max_prefix_sum(a):
    # todo
    return 0

print(max_prefix_sum([3,-5,0,1,100,-2,-5,6]))
print(max_prefix_sum([3,-5,0,1,10,-2,-5,6]))
print(max_prefix_sum([3,-5,0,1,0,-2,-5,6]))


# Entwurfsmuster DaC
#
def max_sum_dac(a):
    m = len(a)                          # O(1)
    # 1. Rekursionsanker
    #
    # 2. Divide
    #
    # 3. Rekursion
    #
    # 4. Conquer
    #
    return 0

a = [3,-5,0,2,100,-2,-5,9]
print(max_sum_all(a))
max_sum_dac(a)

a = [-3,5,-1,2,-5,3]
print(max_sum_all(a))
print(max_sum_dac(a))

a = [13,-5,-1,7,-5,4]
print(max_sum_all(a))
print(max_sum_dac(a))
