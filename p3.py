def revers(string):
    # res=string.split()
    # val=""
    # for i in res:
    #     val+=i[::-1]+" "
    # return val
    val=""
    for i in range(len(string)-1,-1,-1):
        val+=string[i]
    return val


ip='hello welcom to python'
print(revers(ip))
