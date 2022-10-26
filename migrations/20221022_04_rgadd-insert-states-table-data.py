"""
insert states table data
"""

from yoyo import step

__depends__ = {"20221022_03_TTg3A-create-orders-and-states-tables"}

steps = [
    step(
        """
    INSERT INTO store.states (state_identifier, state_code, st_name)
    VALUES
    (1,'AC','Acre'),
    (2,'AL','Alagoas'),
    (3,'AP','Amapa'),
    (4,'AM','Amazonas'),
    (5,'BA','Bahia'),
    (6,'CE','Ceara'),
    (7,'DF','Distrito Federal'),
    (8,'ES','Espirito Santo'),
    (9,'GO','Goias'),
    (10,'MA','Maranhao'),
    (11,'MT','MatoGrosso'),
    (12,'MS','MatoGrosso do Sul'),
    (13,'MG','Minas Gerais'),
    (14,'PA','Para'),
    (15,'PB','Paraiba'),
    (16,'PR','Parana'),
    (17,'PE','Pernambuco'),
    (18,'PI','Piaui'),
    (19,'RJ','Rio de Janeiro'),
    (20,'RN','Rio Grande do Norte'),
    (21,'RS','Rio Grande do Sul'),
    (22,'RO','Rondonia'),
    (23,'RR','Roraima'),
    (24,'SC','Santa Catarina'),
    (25,'SP','Sao Paulo'),
    (26,'SE','Sergipe'),
    (27,'TO','Tocantins')
 """,
        "TRUNCATE TABLE store.states",
    )
]
