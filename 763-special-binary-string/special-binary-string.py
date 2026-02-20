class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        components = []
        
       
        for j, char in enumerate(s):
           
            count += 1 if char == '1' else -1
            
        
            if count == 0:
                    inner_maximized = self.makeLargestSpecial(s[i + 1 : j])
                    components.append('1' + inner_maximized + '0')
                
                
                    i = j + 1
                
       
        components.sort(reverse=True)
        

        return "".join(components)