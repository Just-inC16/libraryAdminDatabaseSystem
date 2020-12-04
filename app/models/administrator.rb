class Administrator < ApplicationRecord 
    has_many :patrons, dependent: :destroy
    private
    def nonEmpty
        if !(title.present? && author.present? && isbn.present? && copies.present?)
            errors.add(:title, ", author, isbn, or copies are empty")
        end
    end
    validate :nonEmpty
    validates_length_of :isbn, is: 10, numericality: { only_integer: true }, message: " is not a 10-digit number" 
    validates :isbn,
        :uniqueness=>{:message=> " is not unique" }
    validates :copies, 
        :numericality=> { :greater_than_or_equal_to => 0,:message=>" is not an integer" }
        
end