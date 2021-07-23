#1 list slice

def slicey_dicey(val , l):
    l[:] = [x for x in l if x != "hlornk"]
    return l


if __name__ == "__main__":
    print(slicey_dicey("hlornk" ,[1,2,3,4,5,6,7,8,9,"hlornk"]))