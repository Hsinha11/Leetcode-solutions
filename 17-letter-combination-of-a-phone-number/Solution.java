import java.util.ArrayList;
import java.util.List;

class Solution {
    
    public static final String[] keypad ={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();  //creates list to store all combinations generated.
        if (digits == null || digits.length() == 0) {   //checks if input is empty or null
           return result;   //returns empty list
        }
        backtrack(digits, 0, new StringBuilder(), result);  //to build combinations
        return result;
    }

    private void backtrack(String digits, int idx, StringBuilder combination, List<String> result) {   //recursive function
        if (idx == digits.length()) {   //used all digits
            result.add(combination.toString());  //add the current combination to the result list
            return;
        }
        String mapping = keypad[digits.charAt(idx) - '0'];
        for (char c : mapping.toCharArray()) {
            combination.append(c);
            backtrack(digits, idx + 1, combination, result);
            combination.deleteCharAt(combination.length() - 1); // backtrack
            //Remove the last letter before trying the next possible letter
        }
    }
}