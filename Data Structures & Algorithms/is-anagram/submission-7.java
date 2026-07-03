class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> ms=new HashMap<>();
        Map<Character, Integer> mt=new HashMap<>();

        for(char sc: s.toCharArray()){
            ms.put(sc, ms.getOrDefault(sc,0)+1);
        }

        for(char tc: t.toCharArray()){
            mt.put(tc, mt.getOrDefault(tc, 0)+1);
        }

        return ms.equals(mt);
    }
}
