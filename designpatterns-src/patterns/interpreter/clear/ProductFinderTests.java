package patterns.interpreter.clear;


import java.util.Iterator;
import java.util.List;

import junit.framework.TestCase;

public class ProductFinderTests extends TestCase {

	private ProductFinder finder; 
	
	private Product fireTruck = new Product("f1234", "Fire Truck", Color.red, 8.95, ProductSize.MEDIUM);
	private Product barbieClassic = new Product("b7654", "Barbie Classic", Color.yellow, 15.95, ProductSize.SMALL);
	private Product frisbee = new Product("f4321", "Frisbee", Color.pink, 9.99, ProductSize.LARGE);
	private Product baseball = new Product("b2343", "Baseball", Color.white, 15.95, ProductSize.NOT_APPLICABLE);
	private Product toyConvertible = new Product("p1112", "Porsche Convertible", Color.red, 230.00, ProductSize.NOT_APPLICABLE);
	
	protected void setUp(){
		finder = new ProductFinder(createProductRepository());
	}
	
	private ProductRepository createProductRepository(){
		ProductRepository repository = new ProductRepository();
		
		repository.add(fireTruck);
		repository.add(barbieClassic);
		
		return repository;
	}
	
	public void testFindByColor(){
		Specification spec = new ColorSpec(Color.red);
		List foundProducts = finder.selectBy(spec);
		
		assertEquals("found 2 red products", 2, foundProducts.size());
		assertTrue("found fireTruck", foundProducts.contains(fireTruck));
		assertTrue("found Toy Porsche Convertible", foundProducts.contains(toyConvertible));
	}
	
	public void testFindByPrice(){
		
		BelowPriceSpec spec = new BelowPriceSpec(8.95f);
		
		List foundProducts = finder.selectBy(spec);
		assertEquals("found product that cost $8.95", 2, foundProducts.size());
		for (Iterator i = foundProducts.iterator(); i.hasNext(); ) {
			Product p = (Product)i.next();
			assertTrue(p.getPrice() == 8.95);
		}
	}
	
	public void textFindByColorSizeAndBelowPrice(){
		ColorSpec colorSpec = new ColorSpec(Color.red);
		BelowPriceSpec priceSpec = new BelowPriceSpec(10.00f);
		AndSpec andSpec = new AndSpec(colorSpec, priceSpec);
		AndSpec spec = new AndSpec(andSpec, priceSpec);
		List foundProducts = finder.selectBy(spec);
	}
	
	public void textFindBelowPriceAvoidingAColor(){
		
		AndSpec spec = new AndSpec(new BelowPriceSpec(9.00f), new NotSpec(new ColorSpec(Color.red)));
		List foundProducts = finder.selectBy(spec);
	}
	
}
