class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>(); 
        boolean dupe = false; 
        for(int i = 0; i < nums.length; i++) { 
            if(map.containsKey(nums[i])) { 
                dupe = true;
            }
            map.put(nums[i], i); 
        }
        return (dupe); 
    }
}