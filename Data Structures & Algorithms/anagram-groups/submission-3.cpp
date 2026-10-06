class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        unordered_set<string> keys;
        for (int i = 0; i < strs.size(); i++){
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            keys.insert(temp);
            mp[temp].push_back(strs[i]);
        }

        vector<vector<string>> result;
        for (string k : keys){
            result.push_back(mp[k]);
        }
        return result;
    }
};
