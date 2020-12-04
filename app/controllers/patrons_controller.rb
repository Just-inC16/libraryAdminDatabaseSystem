class PatronsController < ApplicationController
    def create
        @administrator	=	Administrator.find(params[:administrator_id])
        @patron	=	@administrator.patrons.create(params.require(:patron).permit(:name,	:review))
        redirect_to administrator_path(@administrator)
    end
    def destroy
        @administrator	=	Administrator.find(params[:administrator_id])
        @patron	=	@administrator.patrons.find(params[:id])
        @patron.destroy
        redirect_to administrator_path(@administrator)
    end
end
