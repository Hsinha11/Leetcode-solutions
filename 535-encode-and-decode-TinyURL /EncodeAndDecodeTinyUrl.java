import java.util.HashMap;
import java.util.Map;
import java.util.Random;

class Codec {
    // Maps the 6-character short key to the original long URL (for decoding)
    private final Map<String, String> mapShortToLong;
    // Maps the original long URL to the 6-character short key (for idempotency)
    private final Map<String, String> mapLongToShort;

    // The base URL prefix for all generated tiny URLs
    private static final String BASE_URL = "http://tinyurl.com/";

    // Characters used to generate the random key (62 unique characters)
    private static final String ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    // The fixed length of the short key
    private static final int SHORT_KEY_LENGTH = 6;

    private final Random random;

    /** Initializes the object of the system. */
    public Codec() {
        mapShortToLong = new HashMap<>();
        mapLongToShort = new HashMap<>();
        random = new Random();
    }

    /**
     * Generates a unique, random 6-character key.
     * Uses a do-while loop to ensure no key collisions occur.
     */
    private String generateUniqueKey() {
        StringBuilder sb = new StringBuilder();
        String key = "";
        do {
            sb.setLength(0); // Reset StringBuilder
            for (int i = 0; i < SHORT_KEY_LENGTH; i++) {
                sb.append(ALPHABET.charAt(random.nextInt(ALPHABET.length())));
            }
            key = sb.toString();
        } while (mapShortToLong.containsKey(key)); // Check for collision
        return key;
    }

    /**
     * Encodes a URL to a shortened URL.
     * Time Complexity: O(1) average
     */
    public String encode(String longUrl) {
        // Idempotency check: if already encoded, return existing short URL
        if (mapLongToShort.containsKey(longUrl)) {
            return BASE_URL + mapLongToShort.get(longUrl);
        }

        String shortKey = generateUniqueKey();

        // Store mappings in both directions
        mapLongToShort.put(longUrl, shortKey);
        mapShortToLong.put(shortKey, longUrl);

        return BASE_URL + shortKey;
    }

    /**
     * Decodes a shortened URL to its original URL.
     * Time Complexity: O(1) average
     */
    public String decode(String shortUrl) {
        // Extract the short key by removing the base URL prefix
        String shortKey = shortUrl.replace(BASE_URL, "");

        // Retrieve the original long URL
        return mapShortToLong.get(shortKey);
    }
}
