package br.ic.grasp.expert3;

import java.util.ArrayList;
import java.util.List;

public class Venda {
	
	List<ItemVenda> itens = new ArrayList<ItemVenda>();

	public double total() {
		double total = 0;
		
		
		if (itens.size() > 100) {
			for (ItemVenda itemVenda : itens) {
				total+=itemVenda.subtotalComDesconto();
			}
		}else{
			for (ItemVenda itemVenda : itens) {
				total+=itemVenda.subtotal();
			}
		}
		
		
		
		return total;
	}
}
