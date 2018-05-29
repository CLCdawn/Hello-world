
public class SingleCharacterII {

	public static char singleNumber(char[] characters) {
		char result = 0 ;
		if (characters == null) {
			result = '\0';
		}else {
			for (int i=0;i<characters.length;i++) {
				int time = 0;
				for (int j = 0;j<characters.length;j++) {
					if(characters[i]==characters[j]) {
						time = time +1;
					}
				}
				if (time==1) {
					result = characters[i];
					break;
				}
			}	
		}
		return result;
    }	   
}