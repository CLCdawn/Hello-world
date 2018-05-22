
public class HammingDistance {

	public static int hammingDistance(int x, int y){
		int count = x^y;
		int result = 0;
		String a = Integer.toBinaryString(count);
		for(int i=0;i<a.length();i++){
			if (a.charAt(i)=='\u0031') {
				result = result+1;
			}
		}
		
		return result;
	}
	   
}