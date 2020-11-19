create table tipo_usuario(
    id_tip_usu serial not null,
    tipo_usu varchar(15) not null,
    primary key (id_tip_usu)
);

create table estado_tarea(
    id_est serial not null,
    nombre_est varchar(20),
    primary key (id_est)
);

create table usuario(
	id_usu serial not null,
	nombre_usu varchar(30) not null,
	apellido_usu varchar(30) not null,
	correo_usu varchar(30) not null,
    id_tip_usu serial not null,
	primary key (id_usu),
    foreign key (id_tip_usu) references tipo_usuario (id_tip_usu)
);

create table tarea(
    id_tar serial not null,
    descripcion_tar varchar(100) not null,
    fecha_ape_tar date,
    fecha_cie_tar date,
    id_usu serial not null,
    id_est serial not null,
    primary key (id_tar),
    foreign key (id_usu) references usuario (id_usu),
    foreign key (id_est) references estado_tarea (id_est)    
);