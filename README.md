# genetic-algorithm-examples

## Phrase Generation
### Example 1
_**Target**: "genetic"_   
   
**Population Size**: 20   
**Mutation Rate**: 0.0   
**Max Generations**: 50

![fig](https://user-images.githubusercontent.com/69395924/132857572-d0d9a3e2-3c0c-4ae8-8ffe-d0dcfc36fec0.jpg)

**Result** : No Solution found   

- - -

**Population Size**: 100   
**Mutation Rate**: 0.0   
**Max Generations**: 50

![fig](https://user-images.githubusercontent.com/69395924/132857479-818f788b-dd06-481d-996e-3a42becf0c81.jpg)

**Result** : Solution found for some runs but for others it saturates before.

- - -

**Population Size**: 20   
**Mutation Rate**: 0.1   
**Max Generations**: 500

![fig](https://user-images.githubusercontent.com/69395924/132858435-7fecde65-305e-4625-b17e-7953ffcc63c2.jpg)

**Result** : Solution found for 4 runs out of 5 with a 0.1 mutation rate. But the run of generation it took was large. Let's try with more mutation rate

- - -

**Population Size**: 20   
**Mutation Rate**: 0.2   
**Max Generations**: 500

![fig](https://user-images.githubusercontent.com/69395924/132858905-7b9d779e-fb7e-48e2-8a9a-eb0fe68697df.jpg)

**Result** : Solution was not found. Increase in mutation rate doesn't necessarily improve the algorithm. Now increase the population size and reduce the mutation rate.

- - -

**Population Size**: 100   
**Mutation Rate**: 0.1   
**Max Generations**: 500

![fig](https://user-images.githubusercontent.com/69395924/132859308-65d1c4bb-feda-4e57-afe1-77613f78a24f.jpg)

**Result** : Solution found for all runs. It was able to find solution with less generations.
