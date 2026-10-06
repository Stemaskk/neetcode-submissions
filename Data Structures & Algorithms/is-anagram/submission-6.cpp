class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_multiset<char> seen;
        if (s.size() != t.size()){
            return false;
        }
        for (int i = 0; i < s.size(); i++){
            seen.insert(s[i]);
        }
        for (int i = 0; i < t.size(); i++){
            if(seen.count(t[i]) > 0){
                seen.erase(seen.find(t[i]));
            }
            else{
                return false;
            }
        }
        if (seen.empty()){
            return true;
        }
        return false;
    }
};
