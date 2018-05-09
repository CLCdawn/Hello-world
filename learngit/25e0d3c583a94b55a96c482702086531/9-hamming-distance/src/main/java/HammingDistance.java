
public class HammingDistance {

	public static int hammingDistance(int x, int y){
		int[] list1 = new int[32];
		int[] list2 = new int[32];
		int cnt1 = 0;
		int cnt2 = 0;
		int count = 0;
		
		if (x<0) {
			x = (int)(-x+Math.pow(2, 32));
			list1[31]= 1;
		}
		while (x>0) {
			int a = x%2;
			list1[cnt1] = a;
			x = x/2;
			cnt1 = cnt1+1;
		}
		
		if (y<0) {
			y = (int)(-y+Math.pow(2, 32));
			list2[31]=1;
		}
		while (y>0) {
			int b = y%2;
			list2[cnt2] = b;
			y = y/2;
			cnt2 = cnt2+1;
		}
		for(int i=0;i<32;i++) {
			if (list1[i] != list2[i]) {
				count = count +1;
			}
		}
		return count;
	}
	   
}