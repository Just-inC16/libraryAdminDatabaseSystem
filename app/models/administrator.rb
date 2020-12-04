class Administrator < ApplicationRecord 
    has_many :patrons, dependent: :destroy
    # private
    # def name_or_surname
    #     if !(title.present? && author.present? && isbn.present? && copies.present?)
    #         {message: 'must be abided'}
    #         # errors.add("Title, author, isbn, or copies are empty")
    #         # :msg: "Title, author, isbn, or copies are empty"
    #         # "Title, author, isbn, or copies are empty"
    #         # errors.add(:title, "must be present") unless title.present?
    #         # errors.add(:author, "must be present") unless author.present?
    #     end
    # end
   
    validates :title, :author, :isbn, :copies,
        :presence=> {:message=>"Title, author, isbn, or copies are empty"}
    # validate :name_or_surname
    validates_length_of :isbn, is: 10, numericality: { only_integer: true }, message: " is not a 10-digit number" 
    validates :isbn,
        :uniqueness=>{:message=> " is not unique" }
    validates:copies, 
        :numericality=> {:message=>" is not an integer"}
   
end
