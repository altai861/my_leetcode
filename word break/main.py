

def wordBreak(s, wordDict):
    ss = ""
    for i in range(len(wordDict)):
        
        for j in range(len(wordDict)):
            if i == j:
                continue
            
        


def main():
    s = "leetcode"
    wordDict = ["le", "et", "co", "de"]

    wordBreak(s, wordDict)

if __name__ == "__main__":
    main()