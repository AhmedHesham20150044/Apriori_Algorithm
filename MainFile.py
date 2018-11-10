from aprioriAlgo import Apriori


m_s = int(input("enter min support from 1 to inf >>> "))
m_c = float(input("enter min confides from 0 to 1 >>> "))
obj = Apriori("CoffeeShopTransactions.xlsx", m_s, m_c)
obj.run_algorithm()
