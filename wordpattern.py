
def partern(word):
    print(word)
    output=""
    for i in range(0,len(word)):
        for j in range(0, len(word)):
            if i==0:
                output+=word[j]+" "
            elif i==len(word)-1:
                output += word[(len(word)-1)-j]+" "
            elif j==0:
                output +=word[i]+" "
            elif j==len(word)-1:
                output += word[(len(word)-1)-i]+" "
            elif i==j:
                if i< len(word)/2:
                    output +=word[i]+" "
                else:
                    output += word[(len(word)-1)-i]+" "
            elif i==(len(word)-1)-j:
                if i < len(word)/2:
                    output += word[(len(word)-1)-i]+" "
                else:
                    output += word[i]+" "
            else:
                output +="  "
        output+= "\n"
    return output

if __name__ == "__main__":
    print(partern(input("Enter any word: ")))