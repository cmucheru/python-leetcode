class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
            category = '' 
            bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4 or length*width*height >= 10**9) 
            heavy = (mass >= 100) 
            both =  bulky and heavy
            neither = not (bulky or heavy)
            
            
            if bulky and not heavy:
                category = "Bulky"
            elif heavy and not bulky:
                category = "Heavy"
            elif both:
                category = "Both"
            elif neither:
                category = "Neither"
            return category
            
