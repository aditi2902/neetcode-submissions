class Solution:
    def decodeString(self, s: str) -> str:
        numstack=[]
        strstack=[]
        curnum=0
        curstr=""
        for x in s:
            if x.isdigit():
                curnum=curnum*10+int(x)
            elif x=="[":
                numstack.append(curnum)
                strstack.append(curstr)
                curnum=0
                curstr=""

            elif x=="]":
                rep=numstack.pop()
                prev=strstack.pop()
                curstr=prev+curstr*rep
            else:
                curstr+=x
        return curstr


            