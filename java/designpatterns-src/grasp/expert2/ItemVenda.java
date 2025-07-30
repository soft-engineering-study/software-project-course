package br.ic.grasp.expert2;

public class ItemVenda {

	private EspecificacaoProduto especificacaoProduto = new EspecificacaoProduto();
	private int quantidade = 0;
	
	public EspecificacaoProduto getEspecificacaoProduto() {
		return especificacaoProduto;
	}
	
	public int getQuantidade() {
		return quantidade;
	}
}
