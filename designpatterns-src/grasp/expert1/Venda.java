package br.ic.grasp.expert1;

import java.util.ArrayList;
import java.util.List;

public class Venda {
	
	List<ItemVenda> itens = new ArrayList<ItemVenda>();

	public double total() {
		double total = 0;
		
		
		for (ItemVenda itemVenda : itens) {
			EspecificacaoProduto especificacaoProduto = 
					itemVenda.getEspecificacaoProduto();
			
			double preco = especificacaoProduto.getPreco();
			
			double subtotal = itemVenda.getQuantidade()*preco;
			
			total+=subtotal;
		}
		
		return total;
	}
}
