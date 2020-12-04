Rails.application.routes.draw do
  get 'home_page/index'
  root	'home_page#index'
  get 'administrators/searchPage'
  get 'search', to: "administrators#search"
  get 'administrators/checkoutBook'
  get 'searchForPatron', to: "patrons#searchForPatron"

  resources :administrators do
    resources :patrons
  end
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
