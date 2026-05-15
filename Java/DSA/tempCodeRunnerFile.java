// Swap
                        temp = nums[minIndex];
                        nums[minIndex] = nums[i];
                        nums[i] = temp;

                        // Print Iteration
                        System.out.println();
                        for(int num :  nums){
                            System.out.print(num + " ");
                        }