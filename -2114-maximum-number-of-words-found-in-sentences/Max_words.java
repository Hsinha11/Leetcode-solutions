class Max_words {
    public int mostWordsFound(String[] sentences) {
        int maxWords = 0;

        for (String sentence : sentences) {
            
            String[] words = sentence.split(" ");
            
            maxWords = Math.max(maxWords, words.length);
        }

        return maxWords;
    }
}
