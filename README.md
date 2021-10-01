# genetic-algorithm-examples

## Phrase Generation
**Mutation Technique** : Randomly alter characters by accept reject strategy based on mutation rate.   
**Crossover Technique** : Take random half from both the parents.   

> ### Use Case 1 - Target Phrase: _"genetic"_   
>    
>> **Population Size**: 20   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 50
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/132857572-d0d9a3e2-3c0c-4ae8-8ffe-d0dcfc36fec0.jpg)
>> 
>> **Result** : No Solution found   
>> 
>> - - -
>> 
>> **Population Size**: 100   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 50
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/132857479-818f788b-dd06-481d-996e-3a42becf0c81.jpg)
>> 
>> **Result** : Solution found for some runs but for others it saturates before.
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.1   
>> **Max Generations**: 500
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/132858435-7fecde65-305e-4625-b17e-7953ffcc63c2.jpg)
>> 
>> **Result** : Solution found for 4 runs out of 5 with a 0.1 mutation rate. But the run of generation it took was large. Let's try with more mutation rate
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.2   
>> **Max Generations**: 500
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/132858905-7b9d779e-fb7e-48e2-8a9a-eb0fe68697df.jpg)
>> 
>> **Result** : Solution was not found. Increase in mutation rate doesn't necessarily improve the algorithm. Now increase the population size and reduce the mutation rate.
>> 
>> - - -
>> 
>> **Population Size**: 100   
>> **Mutation Rate**: 0.1   
>> **Max Generations**: 500
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/132859308-65d1c4bb-feda-4e57-afe1-77613f78a24f.jpg)
>> 
>> **Result** : Solution found for all runs. It was able to find solution with less generations.
>> 


> ### Use Case 2 - Target Phrase: _"genetic algorithm"_   
>   
>> **Population Size**: 20   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 100   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135606105-7dcd4d9c-345c-4dbf-be94-71ac7798ba8d.jpg)
>> 
>> **Result** : No Solution found for such a small population size and without mutation.
>> 
>> - - -
>> 
>> **Population Size**: 100   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 100
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135606568-47659c8d-a9a6-433a-b1c8-2d5b11013e0a.jpg)
>> 
>> **Result** : Still no solutions found only by increasing the population size and no mutation. Next lets try to give some mutation starting with small population size.
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.1   
>> **Max Generations**: 500
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135607074-6c81bf18-17fd-4c6b-bf2c-6ea5c8bebc20.jpg)
>> 
>> **Result** : Doesn't do any better. Maybe because the population size is very small. Or else the mutation technique is bad. Now increasing the population size.
>> 
>> - - -
>> 
>> **Population Size**: 100   
>> **Mutation Rate**: 0.1   
>> **Max Generations**: 500
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135608270-3a42732a-dd57-4085-9d4f-4f1e008e5831.jpg)
>> 
>> **Result** : Still no solution found. Maybe it's time to change the crossover technique.
>> 


**Crossover Technique** : Selectively transferring genes from both parents. Transfer those genes that are correct w.r.t the target phrase
> ### Use Case 2 - Target Phrase: _"genetic algorithm"_   
>   
>> **Population Size**: 20   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 50   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135617531-56558470-fd31-487a-8b9b-a7c44e5cc8a4.jpg)
>> 
>> **Result** : Solution found for each run. There is no mutation.
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.1  
>> **Max Generations**: 50   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135617773-6fc4b48c-74ed-42eb-9348-8099844c4116.jpg)
>> 
>> **Result** : Solution found for each run. Here mutation can increase randomness and hence can delay the target reach. Now lets increase the target phrase length.

> ### Use Case 3 - Target Phrase: _"genetic algorithm is a good technique"_   
>   
>> **Population Size**: 20   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 50   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135618274-1f121aa5-fc3b-4a60-99b5-44a9eb7364f1.jpg)
>> 
>> **Result** : Solution found for each run even if I increase the length of the target string. There is no mutation.
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.1  
>> **Max Generations**: 50   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135618430-cad80081-0146-46ba-bd8f-7309be369cd1.jpg)
>> 
>> **Result** : Solution found for each run with mutation.

> ### Use Case 4 - Target Phrase: _"The Genetic Algorithms are evolutionary optimization procedures, inspired by Darwin's theory of evolution, based on the principles of natural selection and genetics. Holland was probably the first to use the crossover and recombination, mutation, and selection in the study of adaptive and artificial systems."_   
>   
>> **Population Size**: 20   
>> **Mutation Rate**: 0.0   
>> **Max Generations**: 50   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135619460-0a49cd8a-4d0d-411c-8160-fcdb575d2e38.jpg)
>> 
>> **Result** : Solution found for each run even if I increase the length of the target string. There is no mutation.
>> 
>> - - -
>> 
>> **Population Size**: 20   
>> **Mutation Rate**: 0.1  
>> **Max Generations**: 500   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135620396-71ad926c-f484-4458-8493-37f525dec9e7.jpg)
>> 
>> **Result** : No solution found with mutation. Lets increase the population size.
>> 
>> - - -
>> 
>> **Population Size**: 50   
>> **Mutation Rate**: 0.05  
>> **Max Generations**: 200   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135621305-8b4db48a-2b7b-43a7-a389-6fe90058b542.jpg)
>> 
>> **Result** : No solution found with mutation.
>> 
>> - - -
>> 
>> **Population Size**: 50   
>> **Mutation Rate**: 0.00  
>> **Max Generations**: 200   
>> 
>> ![fig](https://user-images.githubusercontent.com/69395924/135621583-aa9561a2-a22a-4f48-a7b4-563b38f3c3e6.jpg)
>> 
>> **Result** : **Random mutation not working with selective crossovers**. Without mutation, solutions are found. 

