class Patron < ApplicationRecord
  belongs_to :administrator
  validates :name,   presence: {message: "must not be empty"}
  validates :review, presence: {message: "must not be empty"}
end
