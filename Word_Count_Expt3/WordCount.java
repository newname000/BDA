import java.io.*;
import java.util.*;

public class WordCount {

    // Map function: splits the input text into words and counts occurrences
    public static Map<String, Integer> map(String input) {
        Map<String, Integer> wordCountMap = new HashMap<>();
        String[] words = input.split("\\W+"); // Split by non-word characters
        
        for (String word : words) {
            word = word.toLowerCase(); // Convert to lowercase for uniformity
            if (!word.isEmpty()) {
                wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);
            }
        }
        return wordCountMap;
    }

    // Reduce function: aggregates the counts of words
    public static Map<String, Integer> reduce(List<Map<String, Integer>> maps) {
        Map<String, Integer> finalCountMap = new HashMap<>();
        
        for (Map<String, Integer> map : maps) {
            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                String word = entry.getKey();
                int count = entry.getValue();
                finalCountMap.put(word, finalCountMap.getOrDefault(word, 0) + count);
            }
        }
        return finalCountMap;
    }

    public static void main(String[] args) {
        // Sample input text
        String inputText = "Hello world! Welcome to the world of Hadoop MapReduce. Hadoop is a framework for processing large data sets.";

        // Simulate the Map phase
        Map<String, Integer> mappedResults = map(inputText);
        
        // Collect all maps in a list (simulating multiple mappers)
        List<Map<String, Integer>> mappedResultsList = new ArrayList<>();
        mappedResultsList.add(mappedResults);
        
        // Simulate the Reduce phase
        Map<String, Integer> finalResults = reduce(mappedResultsList);
        
        // Print the results
        System.out.println("Word Count Results:");
        for (Map.Entry<String, Integer> entry : finalResults.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
