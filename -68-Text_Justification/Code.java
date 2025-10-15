import java.util.*;

public class Main {
    static class Solution {
        void addSpaces(StringBuilder str, int count) {
            for (int i = 0; i < count; i++)
                str.append(' ');
        }

        public List<String> fullJustify(String[] words, int maxWidth) {
            List<String> ans = new ArrayList<>();
            int ind = 0, n = words.length;

            while (ind < n) {
                int charsLength = words[ind].length();
                int last = ind + 1;

                while (last < n) {
                    if (charsLength + 1 + words[last].length() > maxWidth)
                        break;
                    charsLength += 1 + words[last].length();
                    last++;
                }

                int diff = last - ind - 1;
                StringBuilder str = new StringBuilder();

                if (diff == 0 || last == n) {
                    for (int i = ind; i < last; i++) {
                        str.append(words[i]);
                        if (i < last - 1) str.append(' ');
                    }
                    addSpaces(str, maxWidth - str.length());
                } else {
                    int spaces = (maxWidth - charsLength) / diff;
                    int remSpaces = (maxWidth - charsLength) % diff;
                    for (int i = ind; i < last; i++) {
                        str.append(words[i]);
                        if (i < last - 1) {
                            int countSpaces = spaces + (i - ind < remSpaces ? 1 : 0);
                            addSpaces(str, 1 + countSpaces);
                        }
                    }
                }

                ans.add(str.toString());
                ind = last;
            }

            return ans;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of words: ");
        int n = sc.nextInt();
        String[] words = new String[n];
        System.out.println("Enter words:");
        for (int i = 0; i < n; i++)
            words[i] = sc.next();

        System.out.print("Enter max width: ");
        int maxWidth = sc.nextInt();

        Solution sol = new Solution();
        List<String> result = sol.fullJustify(words, maxWidth);

        System.out.println("\nJustified Text:");
        for (String line : result)
            System.out.println('"' + line + '"');
    }
}
