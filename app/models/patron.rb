class Patron < ApplicationRecord
  belongs_to :administrator
  validates  :name,   	:presence=>	true
  validates  :review, 	:presence=>	true
end
