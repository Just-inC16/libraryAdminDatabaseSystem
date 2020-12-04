class CreatePatrons < ActiveRecord::Migration[6.0]
  def change
    create_table :patrons do |t|
      t.string :name
      t.text :review
      t.references :administrator, null: false, foreign_key: true

      t.timestamps
    end
  end
end
