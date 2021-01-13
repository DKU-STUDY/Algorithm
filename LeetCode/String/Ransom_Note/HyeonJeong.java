package LeetCode.String.Ransom_Note;

class HyeonJeong {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] n = ransomNote.toCharArray();
        char[] m = magazine.toCharArray();
        int state;
        for (int i = 0; i < ransomNote.length(); i++) {
            state = 0;
            for (int j = 0; j < magazine.length(); j++) {
                if (n[i] == m[j]) {
                    m[j] = ' ';
                    state = 1;
                    break;
                }
            }
            if(state == 0)
                return false;
        }
        return true;
    }
}
