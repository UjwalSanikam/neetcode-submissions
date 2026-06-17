#include <string>
#include <vector>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
            int len1 = s1.length();
                    int len2 = s2.length();
                            
                                    // Base case: s2 cannot contain a permutation of s1 if it is shorter
                                            if (len1 > len2) return false;
                                                    
                                                            // Frequency arrays of size 26 initialized to 0
                                                                    std::vector<int> s1Count(26, 0);
                                                                            std::vector<int> s2Count(26, 0);
                                                                                    
                                                                                            // Initialize the frequencies for s1 and the first window of s2
                                                                                                    for (int i = 0; i < len1; i++) {
                                                                                                                s1Count[s1[i] - 'a']++;
                                                                                                                            s2Count[s2[i] - 'a']++;
                                                                                                                                    }
                                                                                                                                            
                                                                                                                                                    // Check if the first window is already a match
                                                                                                                                                            if (s1Count == s2Count) return true;
                                                                                                                                                                    
                                                                                                                                                                            // Slide the window across the rest of s2
                                                                                                                                                                                    for (int i = 0; i < len2 - len1; i++) {
                                                                                                                                                                                                // Include the next character entering the window
                                                                                                                                                                                                            s2Count[s2[i + len1] - 'a']++;
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                    // Exclude the old character leaving the window
                                                                                                                                                                                                                                                s2Count[s2[i] - 'a']--;
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                        // Compare the frequency vectors
                                                                                                                                                                                                                                                                                    if (s1Count == s2Count) return true;
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                            return false;
                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                };