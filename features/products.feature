Feature: Product Management

Scenario: Read a product
  Given a product exists
  When I read the product
  Then I should see the product

Scenario: Update a product
  Given a product exists
  When I update the product
  Then it should be updated

Scenario: Delete a product
  Given a product exists
  When I delete the product
  Then it should be removed
