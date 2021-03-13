package br.ic.ufal.employees.payments;

@FunctionalInterface
public interface Bonus {
    


    double calculateBonus(int percentage);
    //double calculateExtraBonus(int percentage);

    default double applyBonusOf10(){
        return calculateBonus(10);
    }
}
