from asgiref.sync import sync_to_async
from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from time import sleep

from .models import Court
from .serializers import courtSerializer


class CourtConsumer(AsyncAPIConsumer):
    async def accept(self, **kwargs):
        await super().accept(**kwargs)
        await self.model_change.subscribe()

    @model_observer(Court)
    async def model_change(self, **kwargs):
        data = await self.get_data()
        await self.send_json(data)

    @sync_to_async
    def get_data(self):
        sleep(0.5)
        return courtSerializer(Court.objects.all(), many=True).data
