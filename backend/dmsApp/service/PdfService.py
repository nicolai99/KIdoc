import logging

from django.db.models import Prefetch, Count, Q

from dmsAPI.ProcessingError import ProcessingError
from dmsApp.models import PDFDocument, AttributesValue
from dmsApp.service.ArchiveService import ArchiveService

logger = logging.getLogger(__name__)


class PdfService:
    def getPdfById(self, id: int):
        try:
            return PDFDocument.objects.get(id=id)
        except PDFDocument.DoesNotExist:
            raise ProcessingError("PDF does not exist", 1)

    def getPdfsBySearchValues(self, archiveId: int, searchValues: list):
        logger.info(f"searchList: {searchValues}")

        archiveService = ArchiveService()
        archive = archiveService.getArchiveById(archiveId)
        attributes = archive.attributes
        attribute_ids = list(attributes.values_list("id", flat=True))
        logger.info(f"attribute_ids: {attribute_ids}")

        filters = Q()
        match_criteria = []

        for idx, suchwert in enumerate(searchValues):
            if suchwert is not None:
                try:
                    attribute_id = attribute_ids[idx]
                except IndexError:
                    logger.warning("Suchliste länger als Attribute-Liste")
                    continue

                logger.info(f"Adding filter: attribute_id={attribute_id}, value~={suchwert}")
                filters |= Q(attribute_values__attribute_id=attribute_id,
                             attribute_values__value__icontains=suchwert)
                match_criteria.append(attribute_id)

        expected_count = len(match_criteria)
        logger.info(f"Expected matches: {expected_count}")

        if expected_count == 0:
            return PDFDocument.objects.filter(archive=archive).all()

        pdfs = (
            PDFDocument.objects
            .filter(archive_id=archiveId)
            .filter(filters)
            .annotate(match_count=Count(
                'attribute_values__attribute_id',
                filter=Q(attribute_values__value__isnull=False) & filters,
                distinct=True
            ))
            .filter(match_count=expected_count)
            .prefetch_related(
                Prefetch('attribute_values', queryset=AttributesValue.objects.select_related('attribute'))
            )
        )

        logger.info(pdfs.query)
        for pdf in pdfs:
            logger.info(pdf.name)
        return pdfs
