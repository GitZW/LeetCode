# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树


# leetcode submit region begin(Prohibit modification and deletion)
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        trie = self.trie
        for i in word:
            if i in trie:
                trie = trie[i]
            else:
                trie[i] = dict()
                trie = trie[i]
        trie["is_end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie = self.trie
        for i in word:
            if i not in trie:
                return False
            else:
                trie = trie[i]
        if trie.get("is_end"):
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trie = self.trie
        for i in prefix:
            if i not in trie:
                return False
            else:
                trie = trie[i]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.trie)

param_2 = obj.search("word")
param_3 = obj.startsWith("wo")
