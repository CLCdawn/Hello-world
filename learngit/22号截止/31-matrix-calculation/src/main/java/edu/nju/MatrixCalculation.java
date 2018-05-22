package edu.nju;

import java.util.Scanner;

/**this is the real one.#
 * 实现矩阵的加法、乘法以及控制台输出
 * 其中加法和乘法需要有两种实现方式
 * 1.传入一个矩阵进行2个矩阵的操作
 * 2.从控制台（console）读入一个矩阵，再进行操作
 * 所有的数据均为int型
 * 输入数据均默认为正确数据，不需要对输入数据进行校验
 * @author Ray Liu & Qin Liu
 */
public class MatrixCalculation {
	
	/**
	 * 实现矩阵加法，返回一个新的矩阵
	 * @return result matrix = A + B
	 */
	public int[][] plus(int[][] A, int[][] B){
		int [][] C = new int[A.length][A[0].length];
		for (int i=0;i<A.length;i++){
			for (int j=0; j<A[0].length; j++) {
				C[i][j]=A[i][j]+B[i][j];			
			}
		}
		return C;
	}
	
	/**
	 * 实现矩阵乘法，返回一个新的矩阵
	 * @return result matrix = A * B
	 */
	public int[][] times(int[][] A, int[][] B){
		int a = A.length;
		int b = B[0].length;
		int [][] C = new int[a][b];
		for (int i=0; i<a; i++) {
			for (int j=0; j<b; j++) {
				for (int t=0; t<A[0].length; t++) {
					C[i][j]=A[i][t]*B[t][j]+C[i][j];
				}
			}
		}
		return null;
	}
	
	/**
	 * 从控制台读入矩阵数据，进行矩阵加法，读入数据格式如下：
	 * m n
	 * m * n 的数据方阵，以空格隔开
	 * 连续读入2个矩阵数据
	 * example:
	 * 4 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 4 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 返回一个新的矩阵
	 */
	public int [][] plusFromConsole(){
		Scanner sc = new Scanner(System.in);
		
		//输入第一个矩阵的规格
		String line1 = sc.nextLine();
		String [] list1 = line1.split(" ");
		int lenx = Integer.parseInt(list1[0]);
		int leny = Integer.parseInt(list1[1]);
		int [][] m1 = new int[lenx][leny];
		
		//输入第一个矩阵的内容
		for(int i=0;i<lenx;i++) {
			String[] line = sc.nextLine().split(" ");
			for(int j=0;j<line.length;j++) {
				m1[i][j]=Integer.parseInt(line[j]);
			}
		}
		
		//第二个矩阵的规格
		String line2 = sc.nextLine();
		String [] list2 = line2.split(" ");
		int lenx2 = Integer.parseInt(list2[0]);
		int leny2 = Integer.parseInt(list2[1]);
		int [][] m2 = new int[lenx2][leny2];
		
		//第二个矩阵的内容
		for(int i=0;i<lenx2;i++) {
			String[] line0 = sc.nextLine().split(" ");
			for(int j=0;j<line0.length;j++) {
				m2[i][j]=Integer.parseInt(line0[j]);
			}
		}
		sc.close();
		return plus(m1,m2);
	}
		
	

	/**
	 * 输入格式同上方法相同
	 * 实现矩阵的乘法
	 * 返回一个新的矩阵
	 */
	public int[][] timesFromConsole(){
		Scanner sc2 = new Scanner(System.in);
		
		//第一个矩阵的规格
		String line1 = sc2.nextLine();
		String [] list1 = line1.split(" ");
		int lenx = Integer.parseInt(list1[0]);
		int leny = Integer.parseInt(list1[1]);
		int [][] m1 = new int[lenx][leny];
		//第一个矩阵的内容
		for(int i=0;i<lenx;i++) {
			String[] line = sc2.nextLine().split(" ");
			for(int j=0;j<line.length;j++) {
				m1[i][j]=Integer.parseInt(line[j]);
			}
		}

		//第二个矩阵的规格
		String line2 = sc2.nextLine();
		String [] list2 = line2.split(" ");
		int lenx2 = Integer.parseInt(list2[0]);
		int leny2 = Integer.parseInt(list2[1]);
		int [][] m2 = new int[lenx2][leny2];
		//第二个矩阵的内容
		for(int i=0;i<lenx2;i++) {
			String[] line0 = sc2.nextLine().split(" ");
			for(int j=0;j<line0.length;j++) {
				m2[i][j]=Integer.parseInt(line0[j]);
			}
		}
		sc2.close();
		return times(m1,m2);
	}

	/**
	 * 打印出该矩阵的数据
	 * 起始一个空行，结束一个空行
	 * 矩阵中每一行数据呈一行，数据间以空格隔开
	 * example：
	 *
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 * 1 2 3
	 *
	 */
	public static void print(int [][] A) {
		System.out.println();
		for(int i=0;i<A.length;i++){
			for (int j=0; j<A[0].length; j++) {
				System.out.print(A[i][j]);
				if (j<A[0].length-1){
					System.out.print(" ");
				}else {
					System.out.println();
				}
			}
		}
	}
}
