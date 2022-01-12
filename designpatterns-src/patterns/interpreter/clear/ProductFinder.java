package patterns.interpreter.clear;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ProductFinder {
	
	private ProductRepository repository;

	public ProductFinder(ProductRepository repository) {
		this.repository = repository;
	}

	public List selectBy(Specification spec) {
		List foundProducts = new ArrayList();
		Iterator products = null;
		
		while(products.hasNext()){
			Product product = (Product)products.next();
			if (spec.isSatisfiedBy(product)) {
				foundProducts.add(product);
			}
		}
		
		return foundProducts;
	}
}
